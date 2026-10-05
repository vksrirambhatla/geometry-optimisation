"""Gas-phase DFT optimisation with Psi4; run an IR job afterwards to check minima."""
from common import *

def main():
    p = parser(__doc__); quantum_args(p); a = p.parse_args()
    psi4, mol, out = psi4_setup(a)
    energy, wfn = psi4.optimize(a.method, molecule=mol, return_wfn=True)
    mol.save_xyz_file(str(out/'optimised.xyz'), True)
    dump(out/'energy.json', dict(energy_hartree=float(energy), method=a.method,
        charge=a.charge, multiplicity=a.multiplicity,
        status='optimisation converged; minimum not verified until Hessian calculated'))

if __name__ == '__main__': main()
