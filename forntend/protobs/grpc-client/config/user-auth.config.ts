import { UserAuthClient } from '~/protobs/game_protoc.client'
import transport from './transport'

const authClient = new UserAuthClient(transport);

export default authClient