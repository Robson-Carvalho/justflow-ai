defmodule HubWeb.AlertController do
  use HubWeb, :controller

  def create(conn, %{"message" => message}) do

    IO.puts "\n📢 [AI ALERT RECEIVED]: #{message}\n"


    try do
      HubWeb.Endpoint.broadcast("travel_alerts:lobby", "new_alert", %{body: message})
    rescue
      _ -> IO.puts("⚠️ Aviso: WebSocket ainda não configurado ou ninguém ouvindo.")
    end


    json(conn, %{status: "ok", received: true})
  end
end
