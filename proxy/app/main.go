package main

import (
	"context"
	"fmt"
	"io/fs"
	"io/ioutil"
	"mime"
	"net/http"
	"os"
	"strings"

	pb "github.com/afif1731/UTS_5027221032_Muhammad-Afif/protobs"
	"github.com/afif1731/UTS_5027221032_Muhammad-Afif/third_party"
	"github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
	"github.com/rs/cors"
	"google.golang.org/grpc"
	"google.golang.org/grpc/grpclog"
)

func getOpenAPIHandler() http.Handler {
	mime.AddExtensionType(".svg", "image/svg+xml")
	// Use subdirectory in embedded files
	subFS, err := fs.Sub(third_party.OpenAPI, "OpenAPI")
	if err != nil {
		panic("couldn't create sub filesystem: " + err.Error())
	}
	return http.FileServer(http.FS(subFS))
}

func main() {
	gatewayAddr := "localhost:4000"
	serverAddr := "localhost:6900"
	var err error

	log := grpclog.NewLoggerV2(os.Stdout, ioutil.Discard, ioutil.Discard)
	grpclog.SetLoggerV2(log)

	mux := runtime.NewServeMux()

	err = pb.RegisterUserAuthHandlerFromEndpoint(context.Background(), mux, serverAddr, []grpc.DialOption{grpc.WithInsecure()})

	if err != nil {
		log.Fatal(err)
	}

	err = pb.RegisterGameUserHandlerFromEndpoint(context.Background(), mux, serverAddr, []grpc.DialOption{grpc.WithInsecure()})

	if err != nil {
		log.Fatal(err)
	}

	err = pb.RegisterGameGameHandlerFromEndpoint(context.Background(), mux, serverAddr, []grpc.DialOption{grpc.WithInsecure()})

	if err != nil {
		log.Fatal(err)
	}

	err = pb.RegisterGameRoomHandlerFromEndpoint(context.Background(), mux, serverAddr, []grpc.DialOption{grpc.WithInsecure()})

	if err != nil {
		log.Fatal(err)
	}

	oa := getOpenAPIHandler()

	server := &http.Server{
		Addr: gatewayAddr,
		Handler: http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			if strings.HasPrefix(r.URL.Path, "/") {
				mux.ServeHTTP(w, r)
				return
			}
			oa.ServeHTTP(w, r)
		}),
	}
	server.Handler = cors.AllowAll().Handler(mux)

	log.Info("Serving gRPC-Gateway and OpenAPI Documentation on http://", gatewayAddr)
	log.Fatalln(fmt.Errorf("serving gRPC-Gateway server: %w", server.ListenAndServe()))
}
