using System;
using System.IO;
using System.Text;


namespace CS_Lab1_BASE64
{
    class Program
    {
        static void Main(string[] args)
        {
            string base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

            string sourceFile = @"file.txt";
            string fileToWriteIn = @"file-base64.txt";


            StringBuilder base64Result = new StringBuilder();
            using (BinaryReader reader = new BinaryReader(new FileStream(sourceFile, FileMode.Open, FileAccess.Read)))
            {
                byte[] bytes;
                int[] indices;

                while (true)
                {
                    indices = new int[4];
                    bytes = reader.ReadBytes(3);

                    if (bytes.Length == 0)
                    {
                        break;
                    }

                    for (int i = 0; i < bytes.Length * 8; i++)
                    {
                        if ((bytes[i / 8] & (1 << (7 - i % 8))) != 0)
                        {
                            indices[i / 6] |= (1 << (5 - i % 6));
                        }
                        if (i % 6 == 5 || i == bytes.Length * 8 - 1)
                        {
                            base64Result.Append(base64[indices[i / 6]]);
                        }
                    }

                    if (bytes.Length == 2)
                    {
                        base64Result.Append("=");
                    }
                    else if (bytes.Length == 1)
                    {
                        base64Result.Append("==");
                    }
                }

            }
            //Console.WriteLine(base64Result);

            string base64ResultWithBuiltInFunc = Convert.ToBase64String(File.ReadAllBytes(sourceFile));

            //if our result is similar with built-in function - write it to the file
            if (base64Result.ToString() == base64ResultWithBuiltInFunc)
            {
                using (StreamWriter writer = new StreamWriter(fileToWriteIn, append: false, encoding: Encoding.UTF8))
                {
                    writer.WriteLine(base64Result);
                }
            }


            //Console.ReadLine();
        }
    }
}
