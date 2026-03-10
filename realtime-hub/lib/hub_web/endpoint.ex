defmodule HubWeb.Endpoint do
  use HubWeb, :endpoint

  socket "/socket", HubWeb.UserSocket,
  websocket: [check_origin: false],
  longpoll: false

  plug Plug.Static,
    at: "/",
    from: :hub,
    gzip: false,
    only: ~w(favicon.ico)

  plug Plug.Parsers,
  parsers: [:urlencoded, :multipart, :json],
  pass: ["*/*"],
  json_decoder: Phoenix.json_library()

  plug Plug.Logger
  plug HubWeb.Router

  def start_link(opts) do
    Phoenix.Endpoint.Server.start_link(__MODULE__, opts)
  end

 @impl true
  def init(_key, config) do
    config = config
      |> Keyword.put(:http, [port: 4000, ip: {0, 0, 0, 0}])
      |> Keyword.put(:pubsub_server, Hub.PubSub)

    {:ok, config}
  end
end
