import type { LoginRequest, Loginresponse } from '../game_protoc'
import authConn from './config/user-auth.config'

export const UserAuthController = {
    async login(email: string, password: string) {
        const request: LoginRequest = {
            email: email,
            password: password
        }
        console.log(request)
        const response: Loginresponse = await authConn.login(request).response

        return response
    }
}