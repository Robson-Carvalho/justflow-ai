defmodule Hub.Application do
  use Application

  def start(_type, _args) do
    children = [
      {Phoenix.PubSub, name: Hub.PubSub},
      HubWeb.Endpoint
    ]

    opts = [strategy: :one_for_one, name: Hub.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
