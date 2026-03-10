defmodule HubWeb.PageController do
  use HubWeb, :controller

  def index(conn, _params) do
    json(conn, %{status: "online", message: "JustFlow AI Hub operacional!"})
  end

  def favicon(conn, _params) do
    send_resp(conn, 204, "")
  end
end
