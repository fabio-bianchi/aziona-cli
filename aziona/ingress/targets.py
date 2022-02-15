import sys

from aziona.core import io
from aziona.services.executor import executor


def main(payload) -> bool:
    try:
        # TODO: add json-schema payload validation

        executor.main(payload)
    except KeyboardInterrupt as e:
        io.exception(e)
    except Exception as e:
        io.exception(e)
    else:
        return 0


if __name__ == "__main__":
    sys.exit(main())
