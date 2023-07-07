from django.contrib.admin.templatetags.admin_list import results
from django.shortcuts import render, redirect

from . import models
from .models import PollingUnitResult, PartyResult


def individual_polling_unit_result(request, uniqueid):
    polling_unit = PollingUnitResult.objects.get(uniqueid=uniqueid)
    # Retrieve the results for the polling unit from the announced_pu_results table
    # You may need to define a model for the announced_pu_results table and establish the necessary relationships
    # Pass the retrieved results to the template for rendering
    return render(request, 'individual_polling_unit_result.html', {'polling_unit': polling_unit, 'results': results})


def local_government_result(request):
    if request.method == 'POST':
        lga_id = request.POST.get('lga_id')
        total_result = PollingUnitResult.objects.filter(polling_unit__lga_id=lga_id).aggregate(
            pdp_total=models.Sum('pdp'),
            dpp_total=models.Sum('dpp'),
            acn_total=models.Sum('acn'),
            cdc_total=models.Sum('cdc'),
            jp_total=models.Sum('jp')
        )
        return render(request, 'local_government_result.html', {'total_result': total_result})
    return render(request, 'local_government_form.html')


def form_view(request):
    if request.method == 'POST':
        # Process the form data and calculate the result
        input1 = request.POST.get('input1')
        input2 = request.POST.get('input2')
        result1 = input1 + ' processed'
        result2 = input2 + ' processed'

        # Redirect to the result page with the calculated results
        return redirect('result', result1=result1, result2=result2)

    return render(request, 'form.html')


def result_view(request, result1, result2):
    # Render the result page with the provided result data
    return render(request, 'result.html', {'result1': result1, 'result2': result2})


def create_polling_unit(request):
    if request.method == 'POST':
        uniqueid = request.POST['uniqueid']
        ward_id = request.POST['ward_id']
        lga_id = request.POST['lga_id']
        state_id = request.POST['state_id']
        pdp_votes = request.POST['pdp_votes']
        dpp_votes = request.POST['dpp_votes']
        acn_votes = request.POST['acn_votes']
        cdc_votes = request.POST['cdc_votes']
        jp_votes = request.POST['jp_votes']

        result = PollingUnitResult(
            uniqueid=uniqueid,
            ward_id=ward_id,
            lga_id=lga_id,
            state_id=state_id,
            pdp_votes=pdp_votes,
            dpp_votes=dpp_votes,
            acn_votes=acn_votes,
            cdc_votes=cdc_votes,
            jp_votes=jp_votes
        )
        result.save()

        return redirect('polling_unit_created')

    return render(request, 'create_polling_unit.html')

# Define other views for the remaining questions (summed total result, storing results for all parties)
