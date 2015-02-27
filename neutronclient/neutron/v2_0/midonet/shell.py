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

from neutronclient.neutron.v2_0.midonet import agent_membership
from neutronclient.neutron.v2_0.midonet import cluster

COMMANDS_MIDONET = {
    'cluster-flush': cluster.Flush,
    'cluster-import': cluster.Import,
    'agent-membership-show': agent_membership.Show,
    'agent-membership-list': agent_membership.List,
    'agent-membership-create': agent_membership.Create,
    'agent-membership-delete': agent_membership.Delete
}
