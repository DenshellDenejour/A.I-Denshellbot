from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(3, 3)

qc.h(0)

qc.cx(0, 1)


qc.measure([0, 2], [0, 2])

backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1000)
result = job.result()

counts = result.get_counts()
print(counts)
