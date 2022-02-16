from dataclasses import dataclass, field

from aziona import errors
from aziona.ingress import targets

routes = {
    "targets": {
        "module": targets,
        "properties": targets.__VALIDATOR__PROP__.keys(),
        "validate": targets.validate,
    }
}


@dataclass
class Route:
    @dataclass
    class _Payload:
        index: str
        data: list = field(default_factory=dict)

    module: object = None
    validate: object = None
    properties: list = field(default_factory=dict)
    payload: _Payload = field(default_factory=_Payload)

    def is_valid(self):
        self.validate(self.payload["data"])

    def run(self):
        self.is_valid()
        self.module.main(self.payload)


def get(index: str, data: dict):

    route = routes.get(index, None)
    if route is None:
        raise errors.CriticalError(message=f"Route {index} not foud")

    route.update(payload={"index": index, "data": data})

    return Route(**route)
