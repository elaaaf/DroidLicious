

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;


public class Parser 
{

	static String temp = "";
	final static String space = " ";
	

	public static void main(String[] args) throws IOException
	{
		parse("Benign txt files path");
		parse("Malicious txt files path");
	}
	
	public static void parse(String path) throws IOException {
		ArrayList<String> lines = new ArrayList<String>();
		ArrayList<String> fileNames = new ArrayList<String>();
		listFiles(path, fileNames);
		String FlowDroidResultFile = "";
		String sink = "";
		for (String fileName : fileNames) {
			
			if(fileName.contains(".DS_Store"))
				continue;

			if(fileName.contains(".txt")) 
				 FlowDroidResultFile = fileName.substring(0, fileName.lastIndexOf('_')) + "_P.txt";
			
			BufferedWriter writer = new BufferedWriter(new FileWriter(FlowDroidResultFile));
			BufferedReader flowDroidResultsReader = new BufferedReader(new FileReader(fileName));
			
			String readLine = "";
			String writeLine = "";
			
			try {

				readLine = flowDroidResultsReader.readLine();
				while (!(readLine == null)) {
					boolean read = false;
					if (readLine.matches("Found a flow to sink .*, from the following sources:")) {
						writeLine = readLine;
						
						writeLine = writeLine.replaceFirst(
								".*Found\\sa\\sflow\\sto\\ssink\\s", "");
						writeLine = writeLine
								.replaceFirst(
										"(on line\\s\\d+)*\\, from the following sources:",
										"");
						sink = writeLine;

						readLine = flowDroidResultsReader.readLine();
						read = true;
						ArrayList<String> sources = new ArrayList<String>();
						while (!(readLine == null)
								&& !(readLine
										.matches("Found a flow to sink .*, from the following sources:"))) {
							if (readLine.matches("\\s*-\\s.*")) {
								writeLine = readLine;
								writeLine = writeLine.replaceFirst(">\\)", ">");
								writeLine = writeLine.replaceFirst("\\s*-\\s", "");
								String[] temp = writeLine.split("\\(in ");
								sources.add(temp[0]);
							}
							readLine = flowDroidResultsReader.readLine();
						}
						
						for	(int i = 0; i < sources.size(); i++) {
							if (sources.get(i).contains("@parameter")) 
								  continue;
							  
							  writer.write(sources.get(i).toString().replaceFirst(".*\\$.*<",
							  "<").replaceFirst(">.*", ">").replaceFirst(".*@parameter[0-9]\\:\\s","") +" ~> "+ sink.replaceAll("<init>", "init").replaceFirst(".*<",
							  "<").replaceFirst(">\\(.*\\)",">").replaceFirst("staticinvoke ", ""));
							  writer.newLine();
						}
						
					}

					if (!(read))
						readLine = flowDroidResultsReader.readLine();
				}
				flowDroidResultsReader.close();
				writer.close();


			} catch (IOException e) {
				e.printStackTrace();
			}
			lines.add(writeLine);
		}
	
		System.out.println("finished");
	}
	public static void listFiles(String directoryName, ArrayList<String> files) {
		File directory = new File(directoryName);
		File[] fList = directory.listFiles();
		if (fList != null)
			for (File file : fList) 
					files.add(file.getAbsolutePath());
			
	}
}


 
