from src.modelisation import create__preproc_pipe


def create__preproc_pipe():
    pipe = create__preproc_pipe()
    assert pipe is not None
    assert len(pipe.transformers) ==  2
