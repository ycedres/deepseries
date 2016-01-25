clear
wSizeStart = 10;
wSizeEnd = 14;
step = 5;
table = [];
fileNames = ['minutal_data_sameInstantOfDay_wStart10_wEnd14_h24.mat',
             'minutal_data_sameInstantOfDay_wStart15_wEnd19_h24.mat',
             'minutal_data_sameInstantOfDay_wStart20_wEnd24_h24.mat',
             'minutal_data_sameInstantOfDay_wStart25_wEnd29_h24.mat',
             'minutal_data_sameInstantOfDay_wStart30_wEnd34_h24.mat',
             'minutal_data_sameInstantOfDay_wStart35_wEnd39_h24.mat',
             'minutal_data_sameInstantOfDay_wStart40_wEnd44_h24.mat',
             'minutal_data_sameInstantOfDay_wStart45_wEnd49_h24.mat'];
         
for i = 1:size(fileNames,1)
    file = fileNames(i,:);
    path = strcat('../../data/',file)
    load(path)
    performanceArray=[];
    
    for i=wSizeStart:wSizeEnd
        inputs = eval(strcat('k_',int2str(i),'_inputs'));
        outputs = eval(strcat('k_',int2str(i),'_outputs'));
        nn1;
        performanceArray(i)=performance;
        %save(strcat('resultados_consecutiveDays_',int2str(i)),'errors','hiddenLayerSize','net','performance','targets','tr')
        %clear save(strcat('resultados',int2str(i)),'errors','hiddenLayerSize','net','performance','targets','tr')
        clear inputs
        clear outputs
    end
    
    x=linspace(wSizeStart,wSizeEnd,wSizeEnd-wSizeStart+1);
    perfArray = performanceArray(wSizeStart:wSizeEnd);
    %figure
    %plot(x,perfArray)
    %xlabel('Window Size')
    %ylabel('Performance')

    tmp=[x',perfArray'];
    %save(strcat('perfTable_',int2str(wSizeStart),'_',int2str(wSizeEnd)),table)
    table=[table;tmp];
    wSizeStart = wSizeStart + step;
    wSizeEnd = wSizeEnd + step;
    
end
save('ouput_mse.mat','table')
%myvars = who;
%for i=1:length(myvars)
%    myfunction(eval(myvars(i)))
%end
