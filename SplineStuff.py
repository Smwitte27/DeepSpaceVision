import abc


class State(metaclass=abc.ABCMeta):
    """ State Interface"""
    pass


class ICurvature(metaclass=abc.ABCMeta):
    """Curvature Interface"""
    pass


class IPose2d(metaclass=abc.ABCMeta):
    """Pose Interface"""
    pass


class IRotation2d(metaclass=abc.ABCMeta):
    """Rotation Interface"""
    pass


class ITranslation2d(metaclass=abc.ABCMeta):
    """Translation Interface"""
    pass


class Displacement1d:
    """Displacement Class"""
    pass


class Pose2d(IPose2d):
    """Pose Class"""
    pass


class Pose2dWithCurvature(IPose2d):
    """Pose With Curvature Class"""
    pass


class Rotation2d(IRotation2d):
    """Rotation Class"""
    pass


class Translation2d(ITranslation2d):
    """Translation Class"""
    pass


class Twist2d:
    """Twist Class"""
    pass
