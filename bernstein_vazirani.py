import qiskit

def oracle(n: int, secret_string: str, qc: qiskit.QuantumCircuit, qr: qiskit.QuantumRegister):
    
    """
    Applies the Bernstein-Vazirani oracle to the given quantum circuit.

    This oracle flips the sign of the state |x⟩ based on the value of the secret string bits.
    The secret string is encoded into the oracle which modifies the quantum state.

    Parameters:
        n (int): The number of qubits in the quantum circuit.
        secret_string (str): The binary string representing the secret string (of length n).
        qc (QuantumCircuit): The quantum circuit where the oracle will be applied.
        qr (QuantumRegister): The quantum register where the oracle will act.

    Returns:
        None: The function modifies the provided quantum circuit in place.
    
    Usage:
        import bernstein_vazirani
        bernstein_vazirani.oracle(n, secret_string, qc, qr)
    """

    # Apply the oracle
    for index in range(0,n-1):
        bit = int(secret_string[index])
        if bit == 1:
            qc.z(qr[index])  # Apply Z gate (flips sign) for 1
        elif bit == 0:
            qc.id(qr[index])  # Apply identity gate for 0 (no change)

    # Optional barrier for visual clarity
    qc.barrier()

