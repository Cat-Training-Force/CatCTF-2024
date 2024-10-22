namespace Sleepy;

internal class Program
{
    private static void Main()
    {
        Console.WriteLine("Please input flag: ");
        var flag = Console.ReadLine()!;
        var rand = new Random(114514);
        var pos = 0;
        var buf = new int[(flag.Length + 3) / 4];
        var t = flag.Select(c => (c, r: rand.Next())).Select(t => Task.Run(async () =>
        {
            foreach (var i in Enumerable.Range(0, 8))
            {
                await Task.Delay(t.r);
                var cur = Interlocked.Add(ref pos, 1);
                if ((t.c & (1 << (7 - i))) != 0)
                    Interlocked.Or(ref buf[cur / 32], 1 << (cur % 32));
            }
        }));
        Task.WaitAll(t.ToArray());
        Console.WriteLine(buf.SequenceEqual([
            -970029370, 752772654, 1726752390, -1262080996, -322525652, 216804532, 748467270, 1286907596, -1402172372,
            203164812, -1093923674
        ])
            ? "Right!"
            : "Wrong!");
    }
}