from speechtoolkit.utils.device import device_map


class DistilWhisperModel:
    """
    Use DistilWhisper for automatic speech recognition. Supports significant speedups.

    Supports several speedups (Flash Attention 2 & BetterTransformer), borrowed from [insanely-fast-whisper](https://github.com/Vaibhavs10/insanely-fast-whisper).

    **Args**

    model (str): Which Whisper model to use on the Hugging Face Hub
    device (str): The device to use. Defaults to 'auto'
    use_fa2 (bool): Use Flash Attention 2 (significant speedup). Incompatible with BetterTransformer. Only works on CUDA GPUs.
    use_bettertransformer (bool): Use BetterTransformer (speedup). Incompatible with Flash Attention 2. If available, use Flash Attention 2 instead.
    **kwargs: Additional arguments to pass to Whisper package
    """

    def __init__(
        self,
        model="distil-whisper/distil-large-v3",
        use_fa2=False,
        use_bettertransformer=False,
        device="auto",
        **kwargs,
    ):
        """
        Initialize model.

        **Args**

        model (str): Which Whisper model to use on the Hugging Face Hub
        device (str): The device to use. Defaults to 'auto'
        use_fa2 (bool): Use Flash Attention 2 (significant speedup). Incompatible with BetterTransformer. Only works on CUDA GPUs.
        use_bettertransformer (bool): Use BetterTransformer (speedup). Incompatible with Flash Attention 2. If available, use Flash Attention 2 instead.
        **kwargs: Additional arguments to pass to Whisper package
        """
        if use_bettertransformer and use_fa2:
            raise ValueError(
                "You cannot use both BetterTransformer and Flash Attention 2 at the same time. Typically, Flash Attention 2 provides a better speedup."
            )
        from transformers import pipeline

        model_kwargs = {}
        if use_fa2:
            model_kwargs = {"attn_implementation": "flash_attention_2"}
        self.model = pipeline(
            "automatic-speech-recognition",
            model,
            device=device_map(device),
            model_kwargs=model_kwargs,
            **kwargs,
        )
        if use_bettertransformer:
            self.model.model.to_bettertransformer()

    def infer_file(self, audio_path, **kwargs):
        """
        Run inference on a single file.

        **Args**

        audio_path (str): The path of the original audio.
        **kwargs: Additional arguments to pass to Whisper package

        **Returns**

        str: The transcript of the audio file.
        """
        return self.model(audio_path, **kwargs)["text"].strip()
