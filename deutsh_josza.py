import qiskit
import random
from qiskit.circuit.library import MCXGate

def oracle(n:int,qc:qiskit.QuantumCircuit,aux:qiskit.QuantumRegister):
    
    """
    Applies the Deutsch-Josza oracle to the given quantum circuit.

    Parameters:
        n (int): The number of qubits in the quantum circuit.
        qc (QuantumCircuit): The quantum circuit where the oracle will be applied.
        aux (QuantumRegister): The auxiliary quantum register (if any).

    Returns:
        None: The function modifies the provided quantum circuit in place.
    
    Usage:
        import deutsh_josza
        deutsh_josza.oracle(n, qc, aux)
    """

    # Define the different oracles types

    oracles = ("constant","balanced")
    constant_oracles = ("constant returning zeros f(i)=0","constant returning ones, f(i)=1")
    balanced_oracles = ("Balanced function: f(0) = 0 & f(1) = 1","Balanced function: f(1) = 0 & f(0)=1")

    Random_oracle = random.choice(oracles)

    if Random_oracle == "constant":
        Random_oracle = random.choice(constant_oracles)
    else:
        Random_oracle = random.choice(balanced_oracles)

    if Random_oracle == "constant returning zeros f(i)= 0":
        qc.id(aux)
    elif Random_oracle == "constant returning ones, f(i)= 1":
        qc.x(aux)
    elif Random_oracle == "Balanced function: f(0)= 0 & f(1)= 1":
        qc.cx(i,aux)
    elif Random_oracle == "Balanced function: f(1)= 0 & f(0)= 1":
        for i in range(len(qr)):
            qc.append(MCXGate(1, ctrl_state='0'), [i, aux]) 

    # Optional barrier for visual clarity
    qc.barrier()
    

    