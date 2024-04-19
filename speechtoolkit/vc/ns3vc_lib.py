from speechtoolkit.vc.model import VCModel

class NS3VCModel:
    def __init__(self, device = 'auto', **kwargs,):
        from ns3vc import NS3VC
        self.model = NS3VC(device=device, **kwargs)
    def infer_file(
        self,
        original_audio_path,
        sample_audio_path,
        output_audio_path,
        **kwargs
    ):
        self.model.infer_file(
            original_audio_path,
            sample_audio_path,
            output_audio_path,
            **kwargs
        )