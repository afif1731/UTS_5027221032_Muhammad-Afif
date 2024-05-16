import { GrpcWebFetchTransport } from "@protobuf-ts/grpcweb-transport";

const transport = new GrpcWebFetchTransport({
    baseUrl: useRuntimeConfig().public.SERVER_URI,
    format: 'text'
})

export default transport