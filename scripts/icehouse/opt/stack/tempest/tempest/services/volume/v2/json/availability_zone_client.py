# Copyright 2014 IBM Corp.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from tempest.services.volume.json import availability_zone_client


class VolumeV2AvailabilityZoneClientJSON(
        availability_zone_client.BaseVolumeAvailabilityZoneClientJSON):

    def __init__(self, auth_provider):
        super(VolumeV2AvailabilityZoneClientJSON, self).__init__(
            auth_provider)

        self.api_version = "v2"
