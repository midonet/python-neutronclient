# Copyright 2015 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from neutronclient.neutron import v2_0 as neutronV20

class Create(neutronV20.CreateCommand):

    resource = 'agent_membership'

    def add_known_arguents(self, parser):
        parser.add_argument(
            '--id',
            dest='id', metavar='ID',
            help=_('id of the host.'))
        parser.add_argument(
            '--ip_address',
            dest='ip_address', metavar='IP_ADDRESS',
            help=_('ip address of the host.'))

    def args2body(self, parsed_args):
        body = {self.resource: {}}
        neutronV20.update_dict(parsed_args, body[self.resource],
                               ['id', 'ip_address'])
        return body

class Show(neutronV20.ShowCommand):
    """Show information of a given agent membership."""

    resource = 'agent_membership'

class List(neutronV20.ListCommand):
    """Show information of a given agent membership."""

    resource = 'agent_membership'
    list_columns = ['id', 'ip_address']

class Delete(neutronV20.DeleteCommand):
    """Delete a given agent membership."""

    resource = 'agent_membership'
