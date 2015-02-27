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

from neutronclient.v2_0 import client

APIParamsCall = client.APIParamsCall


class MidonetClient(client.Client):

    clusters_path = "/clusters"

    agent_memberships_path = "/agent_memberships"
    agent_membership_path = "/agent_memberships/%s"

    @APIParamsCall
    def create_cluster(self, body=None):
        return self.post(self.clusters_path, body=body)

    @APIParamsCall
    def create_agent_membership(self, body=None):
        """Creates the specified agent_membership."""
        return self.post(self.agent_memberships_path, body=body)

    @APIParamsCall
    def show_agent_membership(self, agent_membership, **_params):
        """Shows the specified agent_membership."""
        return self.get(self.agent_membership_path % (agent_membership),
                        params=_params)

    @APIParamsCall
    def list_agent_memberships(self, retrieve_all=True, **_params):
        """Lists all agent_memberships."""
        return self.list('agent_memberships', self.agent_memberships_path,
                         retrieve_all, **_params)

    @APIParamsCall
    def delete_agent_membership(self, agent_membership):
        """Deletes the specified agent_membership."""
        return self.delete(self.agent_membership_path % (agent_membership))
