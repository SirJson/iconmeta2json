__all__ = [
    'from_list',
    'from_str',
    'from_int',
    'from_none',
    'from_union',
    'to_class',
    'from_bool',
    'is_type',
    'to_enum',
    'from_dict',
    'ChangeEnum',
    'Free',
    'Search',
    'Brands',
    'SVG',
    'Icon',
    'icons_from_dict',
    'icons_to_dict'
]

# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = icons_from_dict(json.loads(json_string))

from enum import Enum
from dataclasses import dataclass
from typing import List, Any, Optional, Union, Dict, TypeVar, Callable, Type, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return {k: f(v) for (k, v) in x.items()}


class ChangeEnum(Enum):
    THE_31 = "3.1"
    THE_32 = "3.2"
    THE_41 = "4.1"
    THE_42 = "4.2"
    THE_43 = "4.3"
    THE_44 = "4.4"
    THE_45 = "4.5"
    THE_46 = "4.6"
    THE_47 = "4.7"
    THE_500 = "5.0.0"
    THE_501 = "5.0.1"
    THE_5010 = "5.0.10"
    THE_5011 = "5.0.11"
    THE_5012 = "5.0.12"
    THE_5013 = "5.0.13"
    THE_502 = "5.0.2"
    THE_503 = "5.0.3"
    THE_505 = "5.0.5"
    THE_507 = "5.0.7"
    THE_509 = "5.0.9"
    THE_510 = "5.1.0"
    THE_5100 = "5.10.0"
    THE_5101 = "5.10.1"
    THE_5102 = "5.10.2"
    THE_511 = "5.1.1"
    THE_5110 = "5.11.0"
    THE_5111 = "5.11.1"
    THE_5112 = "5.11.2"
    THE_5120 = "5.12.0"
    THE_5121 = "5.12.1"
    THE_5130 = "5.13.0"
    THE_5131 = "5.13.1"
    THE_5140 = "5.14.0"
    THE_520 = "5.2.0"
    THE_530 = "5.3.0"
    THE_540 = "5.4.0"
    THE_541 = "5.4.1"
    THE_542 = "5.4.2"
    THE_550 = "5.5.0"
    THE_560 = "5.6.0"
    THE_561 = "5.6.1"
    THE_563 = "5.6.3"
    THE_570 = "5.7.0"
    THE_580 = "5.8.0"
    THE_581 = "5.8.1"
    THE_582 = "5.8.2"
    THE_590 = "5.9.0"


class Free(Enum):
    BRANDS = "brands"
    REGULAR = "regular"
    SOLID = "solid"


@dataclass
class Search:
    terms: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'Search':
        assert isinstance(obj, dict)
        terms = from_list(from_str, obj.get("terms"))
        return Search(terms)

    def to_dict(self) -> dict:
        result: dict = {}
        result["terms"] = from_list(from_str, self.terms)
        return result


@dataclass
class Brands:
    last_modified: int
    raw: str
    view_box: List[int]
    width: int
    height: int
    path: str

    @staticmethod
    def from_dict(obj: Any) -> 'Brands':
        assert isinstance(obj, dict)
        last_modified = from_int(obj.get("last_modified"))
        raw = from_str(obj.get("raw"))
        view_box = from_list(lambda x: int(from_str(x)), obj.get("viewBox"))
        width = from_int(obj.get("width"))
        height = from_int(obj.get("height"))
        path = from_str(obj.get("path"))
        return Brands(last_modified, raw, view_box, width, height, path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["last_modified"] = from_int(self.last_modified)
        result["raw"] = from_str(self.raw)
        result["viewBox"] = from_list(lambda x: from_str(
            (lambda x: str(x))(x)), self.view_box)
        result["width"] = from_int(self.width)
        result["height"] = from_int(self.height)
        result["path"] = from_str(self.path)
        return result


@dataclass
class SVG:
    brands: Optional[Brands] = None
    solid: Optional[Brands] = None
    regular: Optional[Brands] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SVG':
        assert isinstance(obj, dict)
        brands = from_union([Brands.from_dict, from_none], obj.get("brands"))
        solid = from_union([Brands.from_dict, from_none], obj.get("solid"))
        regular = from_union([Brands.from_dict, from_none], obj.get("regular"))
        return SVG(brands, solid, regular)

    def to_dict(self) -> dict:
        result: dict = {}
        result["brands"] = from_union(
            [lambda x: to_class(Brands, x), from_none], self.brands)
        result["solid"] = from_union(
            [lambda x: to_class(Brands, x), from_none], self.solid)
        result["regular"] = from_union(
            [lambda x: to_class(Brands, x), from_none], self.regular)
        return result


@dataclass
class Icon:
    changes: List[Union[ChangeEnum, int]]
    ligatures: List[str]
    search: Search
    styles: List[Free]
    unicode: str
    label: str
    svg: SVG
    free: List[Free]
    voted: Optional[bool] = None
    private: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Icon':
        assert isinstance(obj, dict)
        changes = from_list(lambda x: from_union([lambda x: from_union(
            [ChangeEnum, lambda x: int(x)], from_str(x))], x), obj.get("changes"))
        ligatures = from_list(from_str, obj.get("ligatures"))
        search = Search.from_dict(obj.get("search"))
        styles = from_list(Free, obj.get("styles"))
        unicode = from_str(obj.get("unicode"))
        label = from_str(obj.get("label"))
        svg = SVG.from_dict(obj.get("svg"))
        free = from_list(Free, obj.get("free"))
        voted = from_union([from_bool, from_none], obj.get("voted"))
        private = from_union([from_bool, from_none], obj.get("private"))
        return Icon(changes, ligatures, search, styles, unicode, label, svg, free, voted, private)

    def to_dict(self) -> dict:
        result: dict = {}
        result["changes"] = from_list(lambda x: from_union([lambda x: from_str((lambda x: to_enum(ChangeEnum, (lambda x: is_type(
            ChangeEnum, x))(x)))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], x), self.changes)
        result["ligatures"] = from_list(from_str, self.ligatures)
        result["search"] = to_class(Search, self.search)
        result["styles"] = from_list(lambda x: to_enum(Free, x), self.styles)
        result["unicode"] = from_str(self.unicode)
        result["label"] = from_str(self.label)
        result["svg"] = to_class(SVG, self.svg)
        result["free"] = from_list(lambda x: to_enum(Free, x), self.free)
        result["voted"] = from_union([from_bool, from_none], self.voted)
        result["private"] = from_union([from_bool, from_none], self.private)
        return result


def icons_from_dict(s: Any) -> Dict[str, Icon]:
    return from_dict(Icon.from_dict, s)


def icons_to_dict(x: Dict[str, Icon]) -> Any:
    return from_dict(lambda x: to_class(Icon, x), x)
