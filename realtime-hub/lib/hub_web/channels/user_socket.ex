defmodule HubWeb.UserSocket do
  use Phoenix.Socket

  channel "travel_alerts:*", HubWeb.AlertChannel

  def connect(_params, socket, _connect_info), do: {:ok, socket}
  
  def id(_socket), do: nil
end
