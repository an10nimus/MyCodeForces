namespace Solution {
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;
    
    operation unitary (qq: Qubit[]) : Unit {
        // ApplyToEach(I, qq); // Then return 0
        // CNOT(qq[0], qq[1]); // Then return 1
        // CNOT(qq[1], qq[0]); // Then return 2
        SWAP(qq[0], qq[1]); // Then return 3
    }

    @EntryPoint()
    operation RunQSharp () : Int {
        mutable m1 = Zero;
        mutable m2 = Zero;
        mutable m3 = Zero;
        mutable m4 = Zero;
        mutable ans = 0;
        using (qubits = Qubit[2]) { // Allocate two qubits in Zero state
            ApplyToEach(X, qubits); // Prepared |11> state
            unitary(qubits);
            set m1 = MResetZ(qubits[0]);
            set m2 = MResetZ(qubits[1]);
        }
        using (qubits2 = Qubit[2]) {
            X(qubits2[1]);  //  Prepared |01> state
            unitary(qubits2);
            set m3 = MResetZ(qubits2[0]);
            Reset(qubits2[1]);
        }
        if (m1 == Zero) {
            set ans = 2;
        } else {
            if (m2 == Zero) {
                set ans = 1;
            } else {
                if (m3 == One) {
                    set ans = 3;
                }
            }
        }
        return ans;
    }
}