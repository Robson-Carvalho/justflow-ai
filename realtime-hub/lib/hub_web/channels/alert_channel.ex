defmodule HubWeb.AlertChannel do
  use HubWeb, :channel

  def join("travel_alerts:lobby", _payload, socket) do
    {:ok, socket}
  end

  def broadcast_alert(message) do
    HubWeb.Endpoint.broadcast("travel_alerts:lobby", "new_alert", %{body: message})
  end
end
