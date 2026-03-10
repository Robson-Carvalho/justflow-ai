FROM elixir:1.15

WORKDIR /app

RUN mix local.hex --force && \
  mix local.rebar --force

COPY mix.exs ./
RUN mix deps.get

COPY . .

RUN mix compile

CMD ["mix", "phx.server"]
