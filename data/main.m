clc, clear, close all
seq = 7;
velP = importdata(strcat('pred', int2str(seq) , '.txt'));
velA = importdata(strcat('actual', int2str(seq) , '.txt'));
posCov = importdata(strcat('seq_CorrPredQ', int2str(seq) , '.txt'));
posP = posCov(:,4:6);
posCov = 1*abs(posCov(:,1:3));
posA = vel2pos(velA);
[N,dim] = size(posP);
posM = posA+(rand(N,3)-0.5)*10;

figure
hold on
plot(posA(:,1), posA(:,3), 'r-.')
plot(posM(:,1), posM(:,3), 'g-.')
plot(posP(:,1), posP(:,3), 'b-.')
grid on

for i = 1:500:N
    index  = i;
    [x,y] = getEllipse(posP(index,1), posP(index,3), posCov(index,1),posCov(index,3));
    plot(posA(index,1), posA(index,3), 'r*', 'MarkerSize', 5)
    plot(posP(index,1), posP(index,3), 'b*', 'MarkerSize', 5)
    plot(x,y, 'b');
end

legend('Ground Truth','Measurement', 'Prediction+Measurement')


axis = 1
figure 
hold on
for i =1:5:length(posA)
    if mod(i,2) == 0
        plot([i, i], [posP(i,axis)  posP(i,axis)+posCov(i,1)], 'b')
        plot([i, i], [posP(i,axis)  posP(i,axis)-posCov(i,1)], 'b')
    else
        plot([i, i], [posP(i,axis)  posP(i,axis)+3*posCov(i,1)], 'g')
        plot([i, i], [posP(i,axis)  posP(i,axis)-3*posCov(i,1)], 'g')
    end
end
plot(posA(:,axis), 'r')
plot(posP(:,axis), 'b')

axis = 3
figure 
hold on
for i =1:5:length(posA)
    if mod(i,2) == 0
        plot([i, i], [posP(i,axis)  posP(i,axis)+posCov(i,1)], 'b')
        plot([i, i], [posP(i,axis)  posP(i,axis)-posCov(i,1)], 'b')
    else
        plot([i, i], [posP(i,axis)  posP(i,axis)+3*posCov(i,1)], 'g')
        plot([i, i], [posP(i,axis)  posP(i,axis)-3*posCov(i,1)], 'g')
    end
end
plot(posA(:,axis), 'r')
plot(posP(:,axis), 'b')
