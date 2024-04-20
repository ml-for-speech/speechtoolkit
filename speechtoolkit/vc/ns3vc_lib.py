class NS3VCModel:
    """
    Use Amphion's NaturalSpeech3 for zero-shot voice conversion

    **Args**

    device (str): The device to use. Defaults to 'auto'
    **kwargs: Additional arguments to pass to package
    """

    def __init__(
        self,
        device="auto",
        **kwargs,
    ):
        """
        Initialize model.

        **Args**

        device (str): The device to use. Defaults to 'auto'
        **kwargs: Additional arguments to pass to package
        """
        from ns3vc import NS3VC

        self.model = NS3VC(device=device, **kwargs)

    def infer_file(
        self, original_audio_path, sample_audio_path, output_audio_path, **kwargs
    ):
        """
        Run inference on a single file.

        **Args**

        original_audio_path (str): The path of the original audio.
        sample_audio_path (str): The path of the speaker sample whose voice you want to clone.
        output_audio_path (str): The path to save your audio
        """
        self.model.infer_file(
            original_audio_path, sample_audio_path, output_audio_path, **kwargs
        )
