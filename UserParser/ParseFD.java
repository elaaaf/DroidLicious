import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;


public class ParseFD {
	
	static String temp = "";
	final static String space = " ";
	

	public static void main(String[] args) throws IOException
	{
		//parse("C:\\Users\\shosho\\DroidLicious\\Components\\Analysis_Output\\Angry_Birds_1_3_5_FD.txt");
		parse(args[0]);
	}
	
	public static void parse(String path) throws IOException {
		String FlowDroidResultFile = "";
		String sink = "";
		if(path.contains(".txt")) 
			FlowDroidResultFile = path.substring(0, path.lastIndexOf('_')) + "_P.txt";
			
			BufferedWriter writer = new BufferedWriter(new FileWriter(FlowDroidResultFile));
			BufferedReader flowDroidResultsReader = new BufferedReader(new FileReader(path));
			
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
								&& !(readLine.matches("Found a flow to sink .*, from the following sources:"))) {
										
							if (readLine.matches("\\s*-\\s.*")) {
								writeLine = readLine;
								writeLine = writeLine.replaceFirst(">\\)", ">");
								writeLine = writeLine.replaceFirst("\\s*-\\s", "");
								//Ask about this one:
								String[] temp = writeLine.split("\\(in ");
								sources.add(temp[0]);
							}
							readLine = flowDroidResultsReader.readLine();
						}
						
						for	(int i = 0; i < sources.size(); i++) {
							//System.out.println(sources.get(i).toString()+" ~> "+ sink);
							if (sources.get(i).contains("@parameter")) {
								  //System.out.println(sources.get(i));
								  continue;
							  }
							  writer.write(sources.get(i).toString().replaceFirst(".*\\$.*<",
							  "<").replaceFirst(">.*", ">").replaceFirst(".*@parameter[0-9]\\:\\s","") +" ~> "+ 
									  sink.replaceAll("<init>", "init").replaceFirst(".*<",
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
			System.out.println("finished");
	}
}
 