# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import dwave_networkx as dnx
from dwave.system.samplers import DWaveSampler

dwave_sampler_pegasus = DWaveSampler(solver={'topology__type': 'pegasus'})
props_pegasus = dwave_sampler_pegasus.properties

# Get total qubits - should be 24 * N * (N - 1)
total_qubits = props_pegasus['num_qubits']

# Get total number of inactive qubits
total_inactive = [i for i in range(total_qubits) if i not in dwave_sampler_pegasus.nodelist]
print(len(total_inactive))

# This should convert the known inactive qubit indices to Pegasus coordinates.
inactive_pegasus_coord = [dnx.pegasus_coordinates(16).linear_to_pegasus(k) for k in total_inactive]

# With coordinates=True, we only get the fabric qubits
pegasus_graph = dnx.pegasus_graph(16, coordinates=True)
active_fabric = [node for node in pegasus_graph.nodes if node not in inactive_pegasus_coord]
print(len(active_fabric))

# another way to compute the number of active qubits
active_qubits = dwave_sampler_pegasus.solver.num_active_qubits
print(active_qubits)
