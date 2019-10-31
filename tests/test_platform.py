import pytest
import os
import glob
import modtox.main as mn

DATA_PATH=os.path.join(os.path.dirname(__file__), "data")
TRAJ=os.path.join(DATA_PATH, "general/traj.pdb")
TOP=os.path.join(DATA_PATH, "general/init.top")
ACTIVE_DUDE=os.path.join(DATA_PATH, "active_decoys/active_dude.sdf")
INACTIVE_DUDE=os.path.join(DATA_PATH, "active_decoys/inactive_dude.sdf")
ACTIVE_PUBCHEM=os.path.join(DATA_PATH, "active_decoys/active_pubchem.sdf")
INACTIVE_PUBCHEM=os.path.join(DATA_PATH, "active_decoys/inactive_pubchem.sdf")
DUDE=os.path.join(DATA_PATH, "dude")
PUBCHEM = os.path.join(DATA_PATH, "pubchem/AID_1851_datatable_all.csv")
SUBSTRATE = "p450-cyp2c9"
FILENAME_MODEL = os.path.join(DATA_PATH, "general/fitted_models.pkl")
FILENAME_MODEL_STACK = os.path.join(DATA_PATH, "general/fitted_models_stack.pkl")
GLIDE_FILES=os.path.join(DATA_PATH, "analysis/input__*dock_lib.maegz")
RESNAME="198"
ACTIVE_ANALYSIS=os.path.join(DATA_PATH, "general/active.sdf")
INACTIVE_ANALYSIS=os.path.join(DATA_PATH, "general/decoys.sdf")

@pytest.mark.parametrize("traj, resname, top, active, inactive", [
                         (TRAJ, RESNAME, TOP, ACTIVE_DUDE, INACTIVE_DUDE),
                         ])
def test_docking(traj, resname, top, active, inactive):
     
    initial_dir = os.getcwd()
    os.chdir(os.path.join(DATA_PATH, "analysis")) 
    mn.main([traj,], resname, active, inactive, top=top, train=True, test=False, dock=True, sieve=1, debug=True)
    os.chdir(initial_dir)


@pytest.mark.parametrize("traj, resname, top, dude", [
                         (TRAJ, RESNAME, TOP, DUDE),
                         ])
def test_dude(traj, resname, top, dude):
    initial_dir = os.getcwd()
    os.chdir(os.path.join(DATA_PATH, "analysis")) 
    mn.main([traj,], resname, dude=dude, train=True, test=False, top=top, dock=True, debug=True)
    os.chdir(initial_dir)

@pytest.mark.parametrize("traj, resname, top, pubchem, substrate", [
                         (TRAJ, RESNAME, TOP, PUBCHEM, SUBSTRATE),
                         ])
def test_pubchem(traj, resname, top, pubchem, substrate):
    
    initial_dir = os.getcwd()
    os.chdir(os.path.join(DATA_PATH, "analysis")) 
  
    mn.main([traj,], resname, pubchem=pubchem, substrate = substrate, top=top, train=True, test=False, dock=True, debug=True, mol_to_read=5)
    
    os.chdir(initial_dir)

@pytest.mark.parametrize("traj, resname, top, active, inactive, filename_model", [
                         (TRAJ, RESNAME, TOP, ACTIVE_DUDE, INACTIVE_DUDE, FILENAME_MODEL_STACK),
                         ])
def test_model_stack(traj, resname, top, active, inactive, filename_model):

     initial_dir = os.getcwd()
     os.chdir(os.path.join(DATA_PATH, "analysis"))
     mn.main(traj, resname, active, inactive, top=top, assemble_model=True, filename_model = filename_model, debug=True, cv=2, train=True, test=False, classifier="stack")
     os.chdir(initial_dir)

@pytest.mark.parametrize("traj, resname, top, active, inactive, filename_model", [
                         (TRAJ, RESNAME, TOP, ACTIVE_ANALYSIS, INACTIVE_ANALYSIS, FILENAME_MODEL),
                         ])
def test_model_normal(traj, resname, top, active, inactive, filename_model):
     initial_dir = os.getcwd()
     os.chdir(os.path.join(DATA_PATH, "analysis"))
     mn.main(traj, resname, active, inactive, top=top, assemble_model=True, filename_model = filename_model, debug=True, cv=2, train=True, test=False)
     os.chdir(initial_dir)

@pytest.mark.parametrize("traj, resname, top, active, inactive, filename_model", [
                         (TRAJ, RESNAME, TOP, ACTIVE_ANALYSIS, INACTIVE_ANALYSIS, FILENAME_MODEL_STACK),
                         ])
def test_model_stack_tpot(traj, resname, top, active, inactive, filename_model):
     initial_dir = os.getcwd()
     os.chdir(os.path.join(DATA_PATH, "analysis"))
     mn.main(traj, resname, active, inactive, top=top, assemble_model=True, filename_model=filename_model, debug=True, cv=2, tpot=True, classifier="stack", test=False, train=True)
     os.chdir(initial_dir)

@pytest.mark.parametrize("traj, resname, top, active, inactive, filename_model", [
                         (TRAJ, RESNAME, TOP, ACTIVE_ANALYSIS, INACTIVE_ANALYSIS, FILENAME_MODEL),
                         ])
def test_model_normal_tpot(traj, resname, top, active, inactive, filename_model):
     initial_dir = os.getcwd()
     os.chdir(os.path.join(DATA_PATH, "analysis"))
     mn.main(traj, resname, active, inactive, top=top, assemble_model=True, filename_model=filename_model, debug=True, cv=2, tpot=True, test=False, train=True)
     os.chdir(initial_dir)

@pytest.mark.parametrize("traj, resname, top, active, inactive, filename_model", [
                         (TRAJ, RESNAME, TOP, ACTIVE_ANALYSIS, INACTIVE_ANALYSIS, FILENAME_MODEL),
                         ])
def test_predict_normal(traj, resname, top, active, inactive, filename_model):
     initial_dir = os.getcwd()
     os.chdir(os.path.join(DATA_PATH, "analysis"))
     mn.main(traj, resname, active, inactive, top=top,filename_model = filename_model, predict=True, train=False, test=True, debug=True)
     os.chdir(initial_dir)

@pytest.mark.parametrize("traj, resname, top, active, inactive, filename_model", [
                         (TRAJ, RESNAME, TOP, ACTIVE_ANALYSIS, INACTIVE_ANALYSIS, FILENAME_MODEL_STACK),
                         ])
def test_predict_stack(traj, resname, top, active, inactive, filename_model):
     initial_dir = os.getcwd()
     os.chdir(os.path.join(DATA_PATH, "analysis"))
     mn.main(traj, resname, active, inactive, top=top,filename_model=filename_model, classifier="stack", train=False, test=True, predict=True, debug=True)
     os.chdir(initial_dir)
