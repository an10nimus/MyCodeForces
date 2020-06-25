namespace Solution {
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;
    
    operation unitary (qq: Qubit) : Unit {
        // H(qq);
        X(qq);
        // ApplyToEach(I, qq); // Then return 0
        // CNOT(qq[0], qq[1]); // Then return 1
        // CNOT(qq[1], qq[0]); // Then return 2
        // SWAP(qq[0], qq[1]); // Then return 3
    }

    @EntryPoint()
    operation RunQSharp () : Int {
        mutable ans = 0;
        using (q = Qubit()) { // Allocate two qubits in Zero state
            H(q);
            unitary(q);
            H(q);
            unitary(q);
            let res = MResetZ(q);
            if (res == One) {
                set ans = 1;
            }
        }
        return ans;
    }
}