import java.io.File;
import java.io.IOException;
import java.nio.file.FileVisitResult;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

import com.google.common.base.Predicate;
import com.google.common.io.Files;
//遍历文件测试
public class FileWalkTest {

	static Collection<File> listFiles(File root){
		List<File> files = new ArrayList<File>();
		listFiles(files, root);
		return files;
	}
	
	static void listFiles(List<File> files, File dir){
		File[] listFiles = dir.listFiles();
		for(File f: listFiles){
			if(f.isFile()){
				files.add(f);
			}else if(f.isDirectory()){
				listFiles(files, f);
			}
		}
	}


	static void run(Runnable task){
		long start = System.currentTimeMillis();
		task.run();
		System.out.printf("用时 %s 毫秒。\n", System.currentTimeMillis() - start);
	}

	public static void main(String[] args){
		String folder = "C:\\Windows\\system32";
		final File dir = new File(folder);
		final Path path = Paths.get(folder);

		//listFiles()
		run(new Runnable(){
			public void run(){
				Collection<File> files = listFiles(dir);
				System.out.printf("通过 listFiles() 共发现 %s 个文件。", files.size());
			}
		});

		
		//plexus utils
		run(new Runnable(){
			public void run(){
				try{
					List<File> files = org.codehaus.plexus.util.FileUtils.getFiles(dir, null, null);
					System.out.printf("通过 Plexus Utils 共发现 %s 个文件。", files.size());
				}catch(IOException e){
					//ignore
				}
			}
		});

		//guava
		run(new Runnable(){
			public void run(){
				int size = Files.fileTreeTraverser().breadthFirstTraversal(dir).filter(new Predicate<File>(){
					public boolean apply(File input) {
						return input.isFile();
					}
				}).size();
				System.out.printf("通过 Guava 共发现 %s 个文件。", size);
			}	
		});

		//commons io
		run(new Runnable(){
			public void run(){
				Collection<File> files = org.apache.commons.io.FileUtils.listFiles(dir, null, true);
				System.out.printf("通过 Commons IO 共发现 %s 个文件。", files.size());
			}
		});

		
		//java 7 nio.2
		run(new Runnable(){
			public void run(){
				final List<File> files = new ArrayList<File>();
				SimpleFileVisitor<Path> finder = new SimpleFileVisitor<Path>(){
					@Override
					public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
						files.add(file.toFile());
						return super.visitFile(file, attrs);
					}
				};
				try{
					java.nio.file.Files.walkFileTree(path, finder);
				}catch(IOException e){
					//ignore
				}
				System.out.printf("通过 Java 7 NIO.2 共发现 %s 个文件。", files.size());
			}
		});
	}
}