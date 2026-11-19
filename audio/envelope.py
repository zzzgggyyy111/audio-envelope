"""音频包络：ADSR、门限与滑音：待实现的核心模块。"""


def adsr(t, attack, decay, sustain, release_start, duration):
    """ADSR 包络。"""
    raise NotImplementedError

def gate(samples, threshold):
    """门限采样下标。"""
    raise NotImplementedError

def velocity_curve(velocity, gamma):
    """力度曲线。"""
    raise NotImplementedError

def portamento(current, target, rate):
    """滑音。"""
    raise NotImplementedError

def release_samples(samples, threshold):
    """释放采样数。"""
    raise NotImplementedError
