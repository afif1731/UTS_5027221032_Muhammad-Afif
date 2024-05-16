from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResponseStatus(_message.Message):
    __slots__ = ("status", "code", "res_msg")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    RES_MSG_FIELD_NUMBER: _ClassVar[int]
    status: bool
    code: int
    res_msg: str
    def __init__(self, status: bool = ..., code: _Optional[int] = ..., res_msg: _Optional[str] = ...) -> None: ...

class ResponseMetadata(_message.Message):
    __slots__ = ("filter", "sort", "limit", "page", "max_page")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_PAGE_FIELD_NUMBER: _ClassVar[int]
    filter: str
    sort: str
    limit: int
    page: int
    max_page: int
    def __init__(self, filter: _Optional[str] = ..., sort: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., max_page: _Optional[int] = ...) -> None: ...

class RegisterRequest(_message.Message):
    __slots__ = ("name", "email", "password")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    name: str
    email: str
    password: str
    def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class RegisterResponse(_message.Message):
    __slots__ = ("status", "data")
    class Data(_message.Message):
        __slots__ = ("token",)
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        token: str
        def __init__(self, token: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    data: RegisterResponse.Data
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ..., data: _Optional[_Union[RegisterResponse.Data, _Mapping]] = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class Loginresponse(_message.Message):
    __slots__ = ("status", "data")
    class Data(_message.Message):
        __slots__ = ("token",)
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        token: str
        def __init__(self, token: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    data: Loginresponse.Data
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ..., data: _Optional[_Union[Loginresponse.Data, _Mapping]] = ...) -> None: ...

class MeRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class MeResponse(_message.Message):
    __slots__ = ("status", "data")
    class Data(_message.Message):
        __slots__ = ("account_id", "user_id", "name")
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        account_id: str
        user_id: str
        name: str
        def __init__(self, account_id: _Optional[str] = ..., user_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    data: MeResponse.Data
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ..., data: _Optional[_Union[MeResponse.Data, _Mapping]] = ...) -> None: ...

class UserDetailRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class UserDetailResponse(_message.Message):
    __slots__ = ("status", "data")
    class Data(_message.Message):
        __slots__ = ("user_id", "user_name", "user_email", "elo", "created_at")
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
        ELO_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        user_id: str
        user_name: str
        user_email: str
        elo: int
        created_at: str
        def __init__(self, user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., user_email: _Optional[str] = ..., elo: _Optional[int] = ..., created_at: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    data: UserDetailResponse.Data
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ..., data: _Optional[_Union[UserDetailResponse.Data, _Mapping]] = ...) -> None: ...

class RecentGameRequest(_message.Message):
    __slots__ = ("account_id", "filter", "sort", "limit", "page")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    filter: str
    sort: str
    limit: int
    page: int
    def __init__(self, account_id: _Optional[str] = ..., filter: _Optional[str] = ..., sort: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class RecentGameResponse(_message.Message):
    __slots__ = ("status", "metadata", "data")
    class Data(_message.Message):
        __slots__ = ("game_id", "player_1", "player_2", "game_type", "is_win", "point")
        GAME_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYER_1_FIELD_NUMBER: _ClassVar[int]
        PLAYER_2_FIELD_NUMBER: _ClassVar[int]
        GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_WIN_FIELD_NUMBER: _ClassVar[int]
        POINT_FIELD_NUMBER: _ClassVar[int]
        game_id: str
        player_1: str
        player_2: str
        game_type: str
        is_win: bool
        point: int
        def __init__(self, game_id: _Optional[str] = ..., player_1: _Optional[str] = ..., player_2: _Optional[str] = ..., game_type: _Optional[str] = ..., is_win: bool = ..., point: _Optional[int] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    metadata: ResponseMetadata
    data: _containers.RepeatedCompositeFieldContainer[RecentGameResponse.Data]
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ..., metadata: _Optional[_Union[ResponseMetadata, _Mapping]] = ..., data: _Optional[_Iterable[_Union[RecentGameResponse.Data, _Mapping]]] = ...) -> None: ...

class LeaderboardRequest(_message.Message):
    __slots__ = ("filter", "sort", "limit", "page")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    filter: str
    sort: str
    limit: str
    page: str
    def __init__(self, filter: _Optional[str] = ..., sort: _Optional[str] = ..., limit: _Optional[str] = ..., page: _Optional[str] = ...) -> None: ...

class LeaderboardResponse(_message.Message):
    __slots__ = ("status", "metadata", "data")
    class Data(_message.Message):
        __slots__ = ("user_id", "user_name", "user_email", "elo", "created_at")
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
        ELO_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        user_id: str
        user_name: str
        user_email: str
        elo: int
        created_at: str
        def __init__(self, user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., user_email: _Optional[str] = ..., elo: _Optional[int] = ..., created_at: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    metadata: ResponseMetadata
    data: _containers.RepeatedCompositeFieldContainer[LeaderboardResponse.Data]
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ..., metadata: _Optional[_Union[ResponseMetadata, _Mapping]] = ..., data: _Optional[_Iterable[_Union[LeaderboardResponse.Data, _Mapping]]] = ...) -> None: ...

class UpdatePasswordRequest(_message.Message):
    __slots__ = ("email", "old_pass", "new_pass")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    OLD_PASS_FIELD_NUMBER: _ClassVar[int]
    NEW_PASS_FIELD_NUMBER: _ClassVar[int]
    email: str
    old_pass: str
    new_pass: str
    def __init__(self, email: _Optional[str] = ..., old_pass: _Optional[str] = ..., new_pass: _Optional[str] = ...) -> None: ...

class UpdatePasswordResponse(_message.Message):
    __slots__ = ("status", "data")
    class Data(_message.Message):
        __slots__ = ("empty_data",)
        EMPTY_DATA_FIELD_NUMBER: _ClassVar[int]
        empty_data: str
        def __init__(self, empty_data: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    data: UpdatePasswordResponse.Data
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ..., data: _Optional[_Union[UpdatePasswordResponse.Data, _Mapping]] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("user_id", "token")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    token: str
    def __init__(self, user_id: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class DeleteUserResponse(_message.Message):
    __slots__ = ("status", "data")
    class Data(_message.Message):
        __slots__ = ("empty_data",)
        EMPTY_DATA_FIELD_NUMBER: _ClassVar[int]
        empty_data: str
        def __init__(self, empty_data: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    data: DeleteUserResponse.Data
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ..., data: _Optional[_Union[DeleteUserResponse.Data, _Mapping]] = ...) -> None: ...

class GameDetailRequest(_message.Message):
    __slots__ = ("game_id",)
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: str
    def __init__(self, game_id: _Optional[str] = ...) -> None: ...

class GameDetailResponse(_message.Message):
    __slots__ = ("status", "data")
    class Data(_message.Message):
        __slots__ = ("game_id", "move_count", "p1_id", "p2_id", "winner", "p1_move", "p2_move", "all_move", "board", "created_at", "duration")
        GAME_ID_FIELD_NUMBER: _ClassVar[int]
        MOVE_COUNT_FIELD_NUMBER: _ClassVar[int]
        P1_ID_FIELD_NUMBER: _ClassVar[int]
        P2_ID_FIELD_NUMBER: _ClassVar[int]
        WINNER_FIELD_NUMBER: _ClassVar[int]
        P1_MOVE_FIELD_NUMBER: _ClassVar[int]
        P2_MOVE_FIELD_NUMBER: _ClassVar[int]
        ALL_MOVE_FIELD_NUMBER: _ClassVar[int]
        BOARD_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        game_id: str
        move_count: int
        p1_id: str
        p2_id: str
        winner: str
        p1_move: _containers.RepeatedScalarFieldContainer[str]
        p2_move: _containers.RepeatedScalarFieldContainer[str]
        all_move: _containers.RepeatedScalarFieldContainer[str]
        board: _containers.RepeatedScalarFieldContainer[str]
        created_at: str
        duration: str
        def __init__(self, game_id: _Optional[str] = ..., move_count: _Optional[int] = ..., p1_id: _Optional[str] = ..., p2_id: _Optional[str] = ..., winner: _Optional[str] = ..., p1_move: _Optional[_Iterable[str]] = ..., p2_move: _Optional[_Iterable[str]] = ..., all_move: _Optional[_Iterable[str]] = ..., board: _Optional[_Iterable[str]] = ..., created_at: _Optional[str] = ..., duration: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    data: GameDetailResponse.Data
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ..., data: _Optional[_Union[GameDetailResponse.Data, _Mapping]] = ...) -> None: ...

class CreateGameRequest(_message.Message):
    __slots__ = ("player_1", "player_2", "game_type")
    PLAYER_1_FIELD_NUMBER: _ClassVar[int]
    PLAYER_2_FIELD_NUMBER: _ClassVar[int]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    player_1: str
    player_2: str
    game_type: str
    def __init__(self, player_1: _Optional[str] = ..., player_2: _Optional[str] = ..., game_type: _Optional[str] = ...) -> None: ...

class CreateGameResponse(_message.Message):
    __slots__ = ("status", "data")
    class Data(_message.Message):
        __slots__ = ("game_id", "game_type", "player1_id", "player1_name", "player2_id", "player2_name", "created_at")
        GAME_ID_FIELD_NUMBER: _ClassVar[int]
        GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
        PLAYER1_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYER1_NAME_FIELD_NUMBER: _ClassVar[int]
        PLAYER2_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYER2_NAME_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        game_id: str
        game_type: str
        player1_id: str
        player1_name: str
        player2_id: str
        player2_name: str
        created_at: str
        def __init__(self, game_id: _Optional[str] = ..., game_type: _Optional[str] = ..., player1_id: _Optional[str] = ..., player1_name: _Optional[str] = ..., player2_id: _Optional[str] = ..., player2_name: _Optional[str] = ..., created_at: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    data: CreateGameResponse.Data
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ..., data: _Optional[_Union[CreateGameResponse.Data, _Mapping]] = ...) -> None: ...

class UpdateMoveRequest(_message.Message):
    __slots__ = ("game_id", "player_type", "move", "board")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_TYPE_FIELD_NUMBER: _ClassVar[int]
    MOVE_FIELD_NUMBER: _ClassVar[int]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    game_id: str
    player_type: int
    move: str
    board: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, game_id: _Optional[str] = ..., player_type: _Optional[int] = ..., move: _Optional[str] = ..., board: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateMoveResponse(_message.Message):
    __slots__ = ("status", "data")
    class Data(_message.Message):
        __slots__ = ("p1_move", "p2_move", "all_move", "board", "move_count")
        P1_MOVE_FIELD_NUMBER: _ClassVar[int]
        P2_MOVE_FIELD_NUMBER: _ClassVar[int]
        ALL_MOVE_FIELD_NUMBER: _ClassVar[int]
        BOARD_FIELD_NUMBER: _ClassVar[int]
        MOVE_COUNT_FIELD_NUMBER: _ClassVar[int]
        p1_move: _containers.RepeatedScalarFieldContainer[str]
        p2_move: _containers.RepeatedScalarFieldContainer[str]
        all_move: _containers.RepeatedScalarFieldContainer[str]
        board: _containers.RepeatedScalarFieldContainer[str]
        move_count: int
        def __init__(self, p1_move: _Optional[_Iterable[str]] = ..., p2_move: _Optional[_Iterable[str]] = ..., all_move: _Optional[_Iterable[str]] = ..., board: _Optional[_Iterable[str]] = ..., move_count: _Optional[int] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    data: UpdateMoveResponse.Data
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ..., data: _Optional[_Union[UpdateMoveResponse.Data, _Mapping]] = ...) -> None: ...

class EndGameRequest(_message.Message):
    __slots__ = ("game_id", "winner")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    WINNER_FIELD_NUMBER: _ClassVar[int]
    game_id: str
    winner: str
    def __init__(self, game_id: _Optional[str] = ..., winner: _Optional[str] = ...) -> None: ...

class EndGameResponse(_message.Message):
    __slots__ = ("status", "data")
    class Data(_message.Message):
        __slots__ = ("game_id", "winner", "duration", "point")
        GAME_ID_FIELD_NUMBER: _ClassVar[int]
        WINNER_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        POINT_FIELD_NUMBER: _ClassVar[int]
        game_id: str
        winner: str
        duration: str
        point: int
        def __init__(self, game_id: _Optional[str] = ..., winner: _Optional[str] = ..., duration: _Optional[str] = ..., point: _Optional[int] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    data: EndGameResponse.Data
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ..., data: _Optional[_Union[EndGameResponse.Data, _Mapping]] = ...) -> None: ...

class BotMoveRequest(_message.Message):
    __slots__ = ("game_id", "board")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    game_id: str
    board: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, game_id: _Optional[str] = ..., board: _Optional[_Iterable[str]] = ...) -> None: ...

class BotMoveResponse(_message.Message):
    __slots__ = ("status", "data")
    class Data(_message.Message):
        __slots__ = ("p1_move", "p2_move", "all_move", "board", "move_count")
        P1_MOVE_FIELD_NUMBER: _ClassVar[int]
        P2_MOVE_FIELD_NUMBER: _ClassVar[int]
        ALL_MOVE_FIELD_NUMBER: _ClassVar[int]
        BOARD_FIELD_NUMBER: _ClassVar[int]
        MOVE_COUNT_FIELD_NUMBER: _ClassVar[int]
        p1_move: _containers.RepeatedScalarFieldContainer[str]
        p2_move: _containers.RepeatedScalarFieldContainer[str]
        all_move: _containers.RepeatedScalarFieldContainer[str]
        board: _containers.RepeatedScalarFieldContainer[str]
        move_count: int
        def __init__(self, p1_move: _Optional[_Iterable[str]] = ..., p2_move: _Optional[_Iterable[str]] = ..., all_move: _Optional[_Iterable[str]] = ..., board: _Optional[_Iterable[str]] = ..., move_count: _Optional[int] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    data: BotMoveResponse.Data
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ..., data: _Optional[_Union[BotMoveResponse.Data, _Mapping]] = ...) -> None: ...

class CreateRoomRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class CreateRoomResponse(_message.Message):
    __slots__ = ("status", "data")
    class Data(_message.Message):
        __slots__ = ("room_id", "creator", "is_wait")
        ROOM_ID_FIELD_NUMBER: _ClassVar[int]
        CREATOR_FIELD_NUMBER: _ClassVar[int]
        IS_WAIT_FIELD_NUMBER: _ClassVar[int]
        room_id: str
        creator: str
        is_wait: bool
        def __init__(self, room_id: _Optional[str] = ..., creator: _Optional[str] = ..., is_wait: bool = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    data: CreateRoomResponse.Data
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ..., data: _Optional[_Union[CreateRoomResponse.Data, _Mapping]] = ...) -> None: ...

class JoinRoomRequest(_message.Message):
    __slots__ = ("user_id", "room_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    room_id: str
    def __init__(self, user_id: _Optional[str] = ..., room_id: _Optional[str] = ...) -> None: ...

class JoinroomResponse(_message.Message):
    __slots__ = ("status", "data")
    class Data(_message.Message):
        __slots__ = ("game_id", "player_1", "player_2")
        GAME_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYER_1_FIELD_NUMBER: _ClassVar[int]
        PLAYER_2_FIELD_NUMBER: _ClassVar[int]
        game_id: str
        player_1: str
        player_2: str
        def __init__(self, game_id: _Optional[str] = ..., player_1: _Optional[str] = ..., player_2: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    data: JoinroomResponse.Data
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ..., data: _Optional[_Union[JoinroomResponse.Data, _Mapping]] = ...) -> None: ...
