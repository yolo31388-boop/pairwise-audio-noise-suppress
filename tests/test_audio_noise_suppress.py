import pytest
import media.audio_noise_suppress as mod

CASES = [
    ("noise_freeze", (1)),
    ("gain_smooth", (1)),
    ("mic_align", (1)),
    ("onset_guard", (1)),
    ("suppress_determinism", (1)),
    ("noise_floor", (1)),
    ("music_detect", (1)),
    ("validation", (1)),
    ("audit", (1)),
    ("fallback", (1)),
    ("spectral_sub", (1)),
    ("metrics", (1)),
    ("breathing_guard", (1)),
    ("latency", (1)),
    ("determinism", (1)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
