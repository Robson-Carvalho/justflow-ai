import { useEffect, useState } from "react";
import { Socket, Channel } from "phoenix";

const WS_URL = import.meta.env.VITE_WS_URL || "ws://localhost:4000/socket";

interface AlertPayload {
  body: string;
}

export const App = () => {
  const [loading, setLoading] = useState(true);
  const [connected, setConnected] = useState(false);
  const [alerts, setAlerts] = useState<string[]>([]);

  useEffect(() => {
    const socket = new Socket(WS_URL);
    socket.connect();

    const channel: Channel = socket.channel("travel_alerts:lobby", {});

    channel
      .join()
      .receive("ok", () => {
        setConnected(true);

        setTimeout(() => setLoading(false), 1200);
      })
      .receive("error", () => setConnected(false));

    channel.on("new_alert", (payload: AlertPayload) => {
      setAlerts((prev) => [payload.body, ...prev].slice(0, 8));
    });

    return () => {
      channel.leave();
      socket.disconnect();
    };
  }, []);

  if (loading) {
    return (
      <div className="flex h-screen w-full flex-col items-center justify-center bg-slate-950">
        <div className="h-12 w-12 animate-spin rounded-full border-4 border-blue-500 border-t-transparent"></div>
        <p className="mt-4 font-mono text-sm tracking-[0.3em] text-blue-400 animate-pulse">
          CONECTANDO AO HUB ELIXIR...
        </p>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-950 p-6 text-slate-200 selection:bg-blue-500/30">
      <div className="mx-auto max-w-5xl">
        <header className="mb-12 flex items-center justify-between border-b border-slate-800 pb-6">
          <div>
            <h1 className="text-3xl font-black tracking-tighter uppercase italic bg-linear-to-r from-blue-500 to-cyan-400 bg-clip-text text-transparent">
              JustFlow IA
            </h1>
            <p className="text-xs font-medium text-slate-500">
              Real-time AI Agent for Travel Market Intelligence
            </p>
          </div>

          <div className="flex items-center gap-3 rounded-full bg-slate-900 px-4 py-1.5 border border-slate-800">
            <div
              className={`h-2 w-2 rounded-full ${connected ? "bg-emerald-500 shadow-[0_0_8px_#10b981]" : "bg-red-500"}`}
            />
            <span className="text-[10px] font-bold uppercase tracking-widest text-slate-400">
              {connected ? "Hub Connected" : "Hub Offline"}
            </span>
          </div>
        </header>

        <main className="grid gap-6">
          <section className="rounded-3xl border border-slate-800 bg-slate-900/50 p-1 backdrop-blur-xl shadow-2xl">
            <div className="rounded-[calc(1.5rem-1px)] bg-slate-900 p-6">
              <div className="mb-6 flex items-center justify-between">
                <h2 className="text-sm font-bold uppercase tracking-widest text-blue-400/80">
                  Live Insights Stream
                </h2>
              </div>

              <div className="space-y-3">
                {alerts.length === 0 ? (
                  <div className="flex h-40 items-center justify-center rounded-2xl border-2 border-dashed border-slate-800 text-slate-600">
                    <p className="text-sm italic">Aguardando Informações...</p>
                  </div>
                ) : (
                  alerts.map((msg, i) => (
                    <div
                      key={i}
                      className="group relative overflow-hidden rounded-xl border border-slate-800 bg-slate-950 p-4 transition-all hover:border-blue-500/50"
                    >
                      <div className="absolute left-0 top-0 h-full w-1 bg-blue-600 opacity-50 transition-all group-hover:opacity-100" />
                      <p className="text-sm leading-relaxed text-slate-300">
                        <span className="mr-2 text-blue-500">▶</span> {msg}
                      </p>
                    </div>
                  ))
                )}
              </div>
            </div>
          </section>
        </main>

        <footer className="mt-8 text-center">
          <p className="text-[10px] font-mono text-slate-700 uppercase tracking-widest">
            &copy; 2026 JUST FLOW
          </p>
        </footer>
      </div>
    </div>
  );
};
