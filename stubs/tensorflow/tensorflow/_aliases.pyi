# Commonly used type aliases.
# Everything in this module is private for stubs. There is no runtime equivalent.

from collections.abc import Iterable, Mapping, Sequence
from typing import Any, Protocol, TypeVar
from typing_extensions import TypeAlias

import numpy as np
import numpy.typing as npt
import tensorflow as tf
from tensorflow.keras.layers import InputSpec

_T = TypeVar("_T")
ContainerGeneric: TypeAlias = Mapping[str, ContainerGeneric[_T]] | Sequence[ContainerGeneric[_T]] | _T

TensorLike: TypeAlias = tf.Tensor | tf.RaggedTensor | tf.SparseTensor
SparseTensorLike: TypeAlias = tf.Tensor | tf.SparseTensor
RaggedTensorLike: TypeAlias = tf.Tensor | tf.RaggedTensor
# _RaggedTensorLikeT = TypeVar("_RaggedTensorLikeT", tf.Tensor, tf.RaggedTensor)
Gradients: TypeAlias = tf.Tensor | tf.IndexedSlices

class KerasSerializable1(Protocol):
    def get_config(self) -> dict[str, Any]: ...

class KerasSerializable2(Protocol):
    __name__: str

KerasSerializable: TypeAlias = KerasSerializable1 | KerasSerializable2

Slice: TypeAlias = int | slice | None
FloatDataSequence: TypeAlias = Sequence[float] | Sequence[FloatDataSequence]
StrDataSequence: TypeAlias = Sequence[str] | Sequence[StrDataSequence]
ScalarTensorCompatible: TypeAlias = tf.Tensor | str | float | np.ndarray[Any, Any] | np.number[Any]

TensorCompatible: TypeAlias = ScalarTensorCompatible | Sequence[TensorCompatible]
# _TensorCompatibleT = TypeVar("_TensorCompatibleT", bound=TensorCompatible)
# Sparse tensors are very annoying. Some operations work on them, but many do not.
# You will need to manually verify if an operation supports them. SparseTensorCompatible is intended to be a
# broader type than TensorCompatible and not all operations will support broader version. If unsure,
# use TensorCompatible instead.
SparseTensorCompatible: TypeAlias = TensorCompatible | tf.SparseTensor

ShapeLike: TypeAlias = tf.TensorShape | Iterable[ScalarTensorCompatible | None] | int | tf.Tensor
DTypeLike: TypeAlias = tf.DType | str | np.dtype[Any] | int

ContainerTensors: TypeAlias = ContainerGeneric[tf.Tensor]
ContainerTensorsLike: TypeAlias = ContainerGeneric[TensorLike]
ContainerTensorCompatible: TypeAlias = ContainerGeneric[TensorCompatible]
ContainerGradients: TypeAlias = ContainerGeneric[Gradients]
ContainerTensorShape: TypeAlias = ContainerGeneric[tf.TensorShape]
ContainerInputSpec: TypeAlias = ContainerGeneric[InputSpec]

AnyArray: TypeAlias = npt.NDArray[Any]
FloatArray: TypeAlias = npt.NDArray[np.float_ | np.float16 | np.float32 | np.float64]
IntArray: TypeAlias = npt.NDArray[np.int_ | np.uint8 | np.int32 | np.int64]
