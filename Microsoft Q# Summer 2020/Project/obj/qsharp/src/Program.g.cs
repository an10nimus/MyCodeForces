//------------------------------------------------------------------------------
// <auto-generated>                                                             
//     This code was generated by a tool.                                       
//     Changes to this file may cause incorrect behavior and will be lost if    
//     the code is regenerated.                                                 
// </auto-generated>                                                            
//------------------------------------------------------------------------------
#pragma warning disable 436
#pragma warning disable 162
#pragma warning disable 1591
using System;
using Microsoft.Quantum.Core;
using Microsoft.Quantum.Intrinsic;
using Microsoft.Quantum.Simulation.Core;

[assembly: CallableDeclaration("{\"Kind\":{\"Case\":\"Operation\"},\"QualifiedName\":{\"Namespace\":\"Solution\",\"Name\":\"unitary\"},\"Attributes\":[],\"Modifiers\":{\"Access\":{\"Case\":\"DefaultAccess\"}},\"SourceFile\":\"C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs\",\"Position\":{\"Item1\":7,\"Item2\":4},\"SymbolRange\":{\"Item1\":{\"Line\":1,\"Column\":11},\"Item2\":{\"Line\":1,\"Column\":18}},\"ArgumentTuple\":{\"Case\":\"QsTuple\",\"Fields\":[[{\"Case\":\"QsTupleItem\",\"Fields\":[{\"VariableName\":{\"Case\":\"ValidName\",\"Fields\":[\"qq\"]},\"Type\":{\"Case\":\"Qubit\"},\"InferredInformation\":{\"IsMutable\":false,\"HasLocalQuantumDependency\":false},\"Position\":{\"Case\":\"Null\"},\"Range\":{\"Item1\":{\"Line\":1,\"Column\":20},\"Item2\":{\"Line\":1,\"Column\":22}}}]}]]},\"Signature\":{\"TypeParameters\":[],\"ArgumentType\":{\"Case\":\"Qubit\"},\"ReturnType\":{\"Case\":\"UnitType\"},\"Information\":{\"Characteristics\":{\"Case\":\"EmptySet\"},\"InferredInformation\":{\"IsSelfAdjoint\":false,\"IsIntrinsic\":false}}},\"Documentation\":[]}")]
[assembly: SpecializationDeclaration("{\"Kind\":{\"Case\":\"QsBody\"},\"TypeArguments\":{\"Case\":\"Null\"},\"Information\":{\"Characteristics\":{\"Case\":\"EmptySet\"},\"InferredInformation\":{\"IsSelfAdjoint\":false,\"IsIntrinsic\":false}},\"Parent\":{\"Namespace\":\"Solution\",\"Name\":\"unitary\"},\"Attributes\":[],\"SourceFile\":\"C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs\",\"Position\":{\"Item1\":7,\"Item2\":4},\"HeaderRange\":{\"Item1\":{\"Line\":1,\"Column\":11},\"Item2\":{\"Line\":1,\"Column\":18}},\"Documentation\":[]}")]
[assembly: CallableDeclaration("{\"Kind\":{\"Case\":\"Operation\"},\"QualifiedName\":{\"Namespace\":\"Solution\",\"Name\":\"RunQSharp\"},\"Attributes\":[{\"TypeId\":{\"Case\":\"Value\",\"Fields\":[{\"Namespace\":\"Microsoft.Quantum.Core\",\"Name\":\"EntryPoint\",\"Range\":{\"Case\":\"Value\",\"Fields\":[{\"Item1\":{\"Line\":1,\"Column\":2},\"Item2\":{\"Line\":1,\"Column\":12}}]}}]},\"Argument\":{\"Item1\":{\"Case\":\"UnitValue\"},\"Item2\":[],\"Item3\":{\"Case\":\"UnitType\"},\"Item4\":{\"IsMutable\":false,\"HasLocalQuantumDependency\":false},\"Item5\":{\"Case\":\"Value\",\"Fields\":[{\"Item1\":{\"Line\":1,\"Column\":12},\"Item2\":{\"Line\":1,\"Column\":14}}]}},\"Offset\":{\"Item1\":16,\"Item2\":4},\"Comments\":{\"OpeningComments\":[],\"ClosingComments\":[]}}],\"Modifiers\":{\"Access\":{\"Case\":\"DefaultAccess\"}},\"SourceFile\":\"C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs\",\"Position\":{\"Item1\":17,\"Item2\":4},\"SymbolRange\":{\"Item1\":{\"Line\":1,\"Column\":11},\"Item2\":{\"Line\":1,\"Column\":20}},\"ArgumentTuple\":{\"Case\":\"QsTuple\",\"Fields\":[[]]},\"Signature\":{\"TypeParameters\":[],\"ArgumentType\":{\"Case\":\"UnitType\"},\"ReturnType\":{\"Case\":\"Int\"},\"Information\":{\"Characteristics\":{\"Case\":\"EmptySet\"},\"InferredInformation\":{\"IsSelfAdjoint\":false,\"IsIntrinsic\":false}}},\"Documentation\":[]}")]
[assembly: SpecializationDeclaration("{\"Kind\":{\"Case\":\"QsBody\"},\"TypeArguments\":{\"Case\":\"Null\"},\"Information\":{\"Characteristics\":{\"Case\":\"EmptySet\"},\"InferredInformation\":{\"IsSelfAdjoint\":false,\"IsIntrinsic\":false}},\"Parent\":{\"Namespace\":\"Solution\",\"Name\":\"RunQSharp\"},\"Attributes\":[],\"SourceFile\":\"C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs\",\"Position\":{\"Item1\":17,\"Item2\":4},\"HeaderRange\":{\"Item1\":{\"Line\":1,\"Column\":11},\"Item2\":{\"Line\":1,\"Column\":20}},\"Documentation\":[]}")]
#line hidden
namespace Solution
{
    [SourceLocation("C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs", OperationFunctor.Body, 8, 18)]
    public partial class unitary : Operation<Qubit, QVoid>, ICallable
    {
        public unitary(IOperationFactory m) : base(m)
        {
        }

        String ICallable.Name => "unitary";
        String ICallable.FullName => "Solution.unitary";
        protected IUnitary<Qubit> MicrosoftQuantumIntrinsicX
        {
            get;
            set;
        }

        public override Func<Qubit, QVoid> Body => (__in__) =>
        {
            var qq = __in__;
#line 10 "C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs"
            MicrosoftQuantumIntrinsicX.Apply(qq);
#line hidden
            return QVoid.Instance;
        }

        ;
        public override void Init()
        {
            this.MicrosoftQuantumIntrinsicX = this.Factory.Get<IUnitary<Qubit>>(typeof(Microsoft.Quantum.Intrinsic.X));
        }

        public override IApplyData __dataIn(Qubit data) => data;
        public override IApplyData __dataOut(QVoid data) => data;
        public static System.Threading.Tasks.Task<QVoid> Run(IOperationFactory __m__, Qubit qq)
        {
            return __m__.Run<unitary, Qubit, QVoid>(qq);
        }
    }

    [SourceLocation("C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs", OperationFunctor.Body, 18, -1)]
    public partial class RunQSharp : Operation<QVoid, Int64>, ICallable
    {
        public RunQSharp(IOperationFactory m) : base(m)
        {
        }

        String ICallable.Name => "RunQSharp";
        String ICallable.FullName => "Solution.RunQSharp";
        public static EntryPointInfo<QVoid, Int64> Info => new EntryPointInfo<QVoid, Int64>(typeof(RunQSharp));
        protected Allocate Allocate
        {
            get;
            set;
        }

        protected Release Release
        {
            get;
            set;
        }

        protected IUnitary<Qubit> MicrosoftQuantumIntrinsicH
        {
            get;
            set;
        }

        protected ICallable<Qubit, QVoid> unitary
        {
            get;
            set;
        }

        protected ICallable<Qubit, Result> MicrosoftQuantumMeasurementMResetZ
        {
            get;
            set;
        }

        public override Func<QVoid, Int64> Body => (__in__) =>
        {
#line 19 "C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs"
            var ans = 0L;
#line hidden
            {
#line 20 "C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs"
                var q = Allocate.Apply();
#line hidden
                bool __arg1__ = true;
                try
                {
#line 21 "C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs"
                    MicrosoftQuantumIntrinsicH.Apply(q);
#line 22 "C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs"
                    unitary.Apply(q);
#line 23 "C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs"
                    MicrosoftQuantumIntrinsicH.Apply(q);
#line 24 "C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs"
                    unitary.Apply(q);
#line 25 "C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs"
                    var res = MicrosoftQuantumMeasurementMResetZ.Apply(q);
#line 26 "C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs"
                    if ((res == Result.One))
                    {
#line 27 "C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs"
                        ans = 1L;
                    }
                }
#line hidden
                catch
                {
                    __arg1__ = false;
                    throw;
                }
#line hidden
                finally
                {
                    if (__arg1__)
                    {
#line hidden
                        Release.Apply(q);
                    }
                }
            }

#line 30 "C:/Users/oskir/Dev/MyCodeForces/Microsoft%20Q%23%20Summer%202020/Project/Program.qs"
            return ans;
        }

        ;
        public override void Init()
        {
            this.Allocate = this.Factory.Get<Allocate>(typeof(Microsoft.Quantum.Intrinsic.Allocate));
            this.Release = this.Factory.Get<Release>(typeof(Microsoft.Quantum.Intrinsic.Release));
            this.MicrosoftQuantumIntrinsicH = this.Factory.Get<IUnitary<Qubit>>(typeof(Microsoft.Quantum.Intrinsic.H));
            this.unitary = this.Factory.Get<ICallable<Qubit, QVoid>>(typeof(unitary));
            this.MicrosoftQuantumMeasurementMResetZ = this.Factory.Get<ICallable<Qubit, Result>>(typeof(Microsoft.Quantum.Measurement.MResetZ));
        }

        public override IApplyData __dataIn(QVoid data) => data;
        public override IApplyData __dataOut(Int64 data) => new QTuple<Int64>(data);
        public static System.Threading.Tasks.Task<Int64> Run(IOperationFactory __m__)
        {
            return __m__.Run<RunQSharp, QVoid, Int64>(QVoid.Instance);
        }
    }
}