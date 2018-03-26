using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace CS_Lab1
{
    class Program
    {
        static void Main(string[] args)
        {
            string sourceFile = @"file.txt";
            string fileToWriteIn = @"file(info).txt";


            int numOfSymbols = 0;
            string fileContent = "";
            Dictionary<char, int> uniqueSymbolsInFile = new Dictionary<char, int>();

            //reading file
            using (StreamReader reader = new StreamReader(sourceFile, Encoding.UTF8))
            {
                fileContent = reader.ReadToEnd();
            }
            //fileContent = fileContent.ToLower();

            //counting number of each symbol and whole number of symbols in file
            foreach (char symbol in fileContent)
            {
                if (uniqueSymbolsInFile.ContainsKey(symbol))
                {
                    uniqueSymbolsInFile[symbol]++;
                }
                else
                {
                    uniqueSymbolsInFile.Add(symbol, 1);
                }
                numOfSymbols++;
            }

            //count average entropy and write it in the file
            using (StreamWriter writer = new StreamWriter(fileToWriteIn, append: false, encoding: Encoding.UTF8))
            {
                double H = 0;
                double p = 0;
                writer.WriteLine("Number of all symbols:  " + numOfSymbols);
                writer.WriteLine();
                foreach (var keyValue in uniqueSymbolsInFile.OrderBy(s => s.Key))
                {
                    p = (double)keyValue.Value / numOfSymbols;
                    //average entropy
                    H += p * Math.Log(1 / p, 2);

                    //writer.WriteLine(keyValue.Key + "  ->  " + keyValue.Value + ",  Відносна частота появи -  " + p);
                    if (keyValue.Key == '\n')
                    {
                        writer.WriteLine("Відносна частота появи \\n  -  " + p);
                    }   
                    else if (keyValue.Key == '\r')
                    {
                        writer.WriteLine("Відносна частота появи \\r  -  " + p);
                    }
                    else if (keyValue.Key == ' ')
                    {
                        writer.WriteLine("Відносна частота появи SPACE  -  " + p);
                    }
                    else
                    {
                        writer.WriteLine("Відносна частота появи " + keyValue.Key + "  -  " + p);
                    }
                }
                writer.WriteLine();
                writer.WriteLine("Everage entropy:  " + H);
                writer.WriteLine();
                writer.WriteLine("Amount of information:  " + H * numOfSymbols + " bits   =   " + H * numOfSymbols / 8 + " bytes");
                writer.WriteLine();
                writer.WriteLine("File size:  " + new FileInfo(sourceFile).Length);
            }
        }

    }
}
