defmodule HubWeb.Router do
  use HubWeb, :router

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/api", HubWeb do
    pipe_through :api

    post "/alerts", AlertController, :create
  end

  scope "/", HubWeb do
    pipe_through :api
    get "/", PageController, :index
    get "/favicon.ico", HubWeb.PageController, :favicon
  end
end
