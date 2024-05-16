import type { Loginresponse_Data, ResponseStatus } from "~/protobs/game_protoc"
import { UserAuthController } from "~/protobs/grpc-client/user-auth.client"

export const GameAuth = {
    async login(email: string, password: string) {
        try {
            const result = await UserAuthController.login(email, password)

            if(!result) {
                console.log('GRPC ERROR')
                throw Error('SOMETHING WRONG')
            }

            const response = {
                status: result.status as ResponseStatus,
                data: result.data as Loginresponse_Data
            }
            
            return response
        } catch(err) {
            console.log(err)
        }
    }
}