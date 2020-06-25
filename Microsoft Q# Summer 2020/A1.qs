namespace Solution {
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;
    
    operation unitary (qq: Qubit[]) : Unit {
        // CNOT(qq[0], qq[1]); // Then return 0
        CNOT(qq[1], qq[0]); // Then return 1
    }

    @EntryPoint()
    operation RunQSharp () : Int {
        mutable ans = 0;
        using (qubits = Qubit[2]) { // Allocate two qubits in Zero state
            ApplyToEach(X, qubits);
            unitary(qubits);
            Reset(qubits[0]);
            let measure2 = MResetZ(qubits[1]);
            if (measure2 == One) {  // Then we have CNOT
                set ans = 1;
            }
        }
        
        return ans;
    }
}