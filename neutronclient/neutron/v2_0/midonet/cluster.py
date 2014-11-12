# Copyright 2014 OpenStack Foundation
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
from neutronclient.openstack.common.gettextutils import _


class CreateCluster(neutronV20.CreateCommand):

    resource = 'cluster'

    def add_known_arguments(self, parser):
       pass

    def args2body(self, parsed_args):
        body = {'cluster': {}}
        if parsed_args.tenant_id:
            body[self.resource].update({'tenant_id': parsed_args.tenant_id})
        return body
