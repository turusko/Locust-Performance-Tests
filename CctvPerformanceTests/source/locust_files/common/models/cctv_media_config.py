import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class CCTVMediaConfig:
    digitalMediaByteStream: str
    fileExtension: str
    toolKitNoticeNumber: str
    stillImage: bool
