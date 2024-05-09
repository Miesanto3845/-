using System;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

class SimpleHTTPServer
{
    private readonly string rootDirectory;
    private readonly TcpListener listener;

    public SimpleHTTPServer(string rootDirectory, int port)
    {
        this.rootDirectory = rootDirectory;
        listener = new TcpListener(IPAddress.Any, port);
    }

    public void Start()
    {
        listener.Start();
        Console.WriteLine($"Server started. Listening on port {((IPEndPoint)listener.LocalEndpoint).Port}...");

        while (true)
        {
            var client = listener.AcceptTcpClient();
            Task.Run(() => ProcessClient(client));
        }
    }

    private void ProcessClient(TcpClient client)
    {
        using (var stream = client.GetStream())
        using (var reader = new StreamReader(stream))
        using (var writer = new StreamWriter(stream))
        {
            var request = reader.ReadLine();
            if (request != null)
            {
                Console.WriteLine($"Request: {request}");
                var parts = request.Split(' ');
                var path = parts[1].Substring(1);
                ServeFile(writer, path);
            }
        }

        client.Close();
    }

    private void ServeFile(StreamWriter writer, string path)
    {
        try
        {
            var fullPath = Path.Combine(rootDirectory, path);
            var content = File.ReadAllText(fullPath);
            var response = $"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {content.Length}\r\n\r\n{content}";
            writer.Write(response);
            Console.WriteLine($"Response: {response}");
        }
        catch (Exception)
        {
            var response = "HTTP/1.1 404 Not Found\r\n\r\n";
            writer.Write(response);
            Console.WriteLine($"Response: {response}");
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Приклад використання:
        var server = new SimpleHTTPServer("C:/WebServerRoot", 8080);
        server.Start();
    }
}
