## Overview

gRPC-Web provides a Javascript client library that enables browser clients to
access a gRPC server.

The current release is a Pre-Alpha release, mainly for early adopters to provide
feedback on the JS API (both gRPC and Protobuf). The JS client library has been
used by Google (Alphabet) projects with Closure compiler and its TypeScript
generator (not yet open-sourced). The use of Closure compiler may or may not fit
your JS development environment.

The gateway that connects the client to the server uses Nginx. However, Nginx
still doesn't support HTTP/2 (to backends) as of Q2/2017, and therefore the
gateway can't be used as a reverse proxy (for load balancing). We have also
added the gRPC-Web support to [Envoy](https://github.com/lyft/envoy). In future,
we expect gRPC-Web to be supported in language-specific Web frameworks, such as
Go, Java, Node, which will eliminate the need to deploy a gateway.

We expect to ship an alpha version in Q3/2017. Stay tuned! [Sign-up form](https://docs.google.com/forms/d/15iRDHoP-VBenc4hWgKn7bk7IirJLgs0uh88nw1vi_Hc/viewform?edit_requested=true).

For questions, please file an issue or contact varuntalwar@google.com.

## Generate and use the client library

Please check the end-to-end echo example in [net/grpc/gateway/examples/echo](https://github.com/grpc/grpc-web/tree/master/net/grpc/gateway/examples/echo).

## Build the gateway

### Ubuntu 14.04

1.  Install docker.
2.  run `./ubuntu\_14\_04.sh`
3.  build result is available in net/grpc/gateway/docker folder as
    gConnector.zip and gConnector_static.zip.

### Mac OS X

1.  Install brew.
2.  `brew install autoconf automake libtool pcre`
3.  run `./darwin\_x86\_64.sh`
4.  build result is available in the root folder as gConnector.zip and
    gConnector_static.zip.
