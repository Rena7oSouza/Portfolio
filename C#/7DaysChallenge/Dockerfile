FROM mcr.microsoft.com/dotnet/sdk:8.0
WORKDIR /app
COPY . ./
RUN dotnet restore
RUN dotnet build -c Release

RUN dotnet publish -c Release -o out
ENTRYPOINT ["dotnet", "out/7DaysChallenge.dll"]
